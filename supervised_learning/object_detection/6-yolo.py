#!/usr/bin/env python3
""" Yolo v3 algorithm to perform object detectio """
import tensorflow.keras as K
import numpy as np
import cv2
import glob
import os


class Yolo:
    """
        Class Yolo that uses the Yolo v3 algorithm to
        perform object detection
    """

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """ Class Constructor. """
        self.model = K.models.load_model(model_path)
        with open(classes_path, 'r') as f:
            self.class_names = [line.strip() for line in f]
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    def sigmoid(self, x):
        """ Sigmoid function """
        return (1 / (1 + np.exp(-x)))

    def process_outputs(self, outputs, image_size):
        """ Process the outputs of the class """
        boxes = [pred[:, :, :, 0:4] for pred in outputs]
        for ipred, pred in enumerate(boxes):
            for grid_h in range(pred.shape[0]):
                for grid_w in range(pred.shape[1]):
                    bx = ((self.sigmoid(pred[grid_h, grid_w, :, 0]) + grid_w)
                          / pred.shape[1])
                    by = ((self.sigmoid(pred[grid_h, grid_w, :, 1]) + grid_h)
                          / pred.shape[0])
                    anchor_tensor = self.anchors[ipred].astype(float)
                    anchor_tensor[:, 0] *= np.exp(pred[grid_h, grid_w, :, 2])\
                        / self.model.input.shape[1].value
                    anchor_tensor[:, 1] *= np.exp(pred[grid_h, grid_w, :, 3])\
                        / self.model.input.shape[2].value
                    pred[grid_h, grid_w, :, 0] = (bx - (anchor_tensor[:, 0] /
                                                  2)) * image_size[1]
                    pred[grid_h, grid_w, :, 1] = (by - (anchor_tensor[:, 1] /
                                                  2)) * image_size[0]
                    pred[grid_h, grid_w, :, 2] = (bx + (anchor_tensor[:, 0] /
                                                  2)) * image_size[1]
                    pred[grid_h, grid_w, :, 3] = (by + (anchor_tensor[:, 1] /
                                                  2)) * image_size[0]
        box_confidences = [self.sigmoid(pred[:, :, :, 4:5]) for pred in
                           outputs]
        box_class_probs = [self.sigmoid(pred[:, :, :, 5:]) for pred in outputs]
        return (boxes, box_confidences, box_class_probs)

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        """ Filter boxes """
        box_score = []
        bc = box_confidences
        bcp = box_class_probs
        for box_conf, box_probs in zip(bc, bcp):
            score = (box_conf * box_probs)
            box_score.append(score)
        box_classes = [s.argmax(axis=-1) for s in box_score]
        box_class_l = [b.reshape(-1) for b in box_classes]
        box_classes = np.concatenate(box_class_l)
        box_class_scores = [s.max(axis=-1) for s in box_score]
        b_scores_l = [b.reshape(-1) for b in box_class_scores]
        box_class_scores = np.concatenate(b_scores_l)
        mask = np.where(box_class_scores >= self.class_t)
        boxes_all = [b.reshape(-1, 4) for b in boxes]
        boxes_all = np.concatenate(boxes_all)
        return (boxes_all[mask], box_classes[mask], box_class_scores[mask])

    def non_max_suppression(self, filtered_boxes, box_classes, box_scores):
        """ Non-max Supression """
        f = []
        c = []
        s = []
        for i in (np.unique(box_classes)):
            idx = np.where(box_classes == i)
            filters = filtered_boxes[idx]
            scores = box_scores[idx]
            classes = box_classes[idx]
            keep = self.nms(filters, self.nms_t, scores)
            filters = filters[keep]
            scores = scores[keep]
            classes = classes[keep]
            f.append(filters)
            c.append(classes)
            s.append(scores)
        return (np.concatenate(f, axis=0), np.concatenate(c, axis=0),
                np.concatenate(s, axis=0))

    def nms(self, boxes, thresh, scores):
        """ Compute the index of the bounding box """
        x1 = boxes[:, 0]
        y1 = boxes[:, 1]
        x2 = boxes[:, 2]
        y2 = boxes[:, 3]
        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        order = scores.argsort()[::-1]
        keep = []
        while (order.size > 0):
            i = order[0]
            keep.append(i)
            xx1 = np.maximum(x1[i], x1[order[1:]])
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])
            w = np.maximum(0.0, xx2 - xx1 + 1)
            h = np.maximum(0.0, yy2 - yy1 + 1)
            inter = w * h
            ovr = inter / (areas[i] + areas[order[1:]] - inter)
            inds = np.where(ovr <= thresh)[0]
            order = order[inds + 1]
        return keep

    @staticmethod
    def load_images(folder_path):
        """ Load images """
        images = []
        image_paths = glob.glob(folder_path + '/*', recursive=False)
        for image in image_paths:
            images.append(cv2.imread(image))
        return (images, image_paths)

    def preprocess_images(self, images):
        """ Preprocess images """
        pimages = []
        shapes = []
        input_h = self.model.input.shape[2].value
        input_w = self.model.input.shape[1].value
        for i in images:
            img_shape = i.shape[0], i.shape[1]
            shapes.append(img_shape)
            image = cv2.resize(i, (input_w, input_h), interpolation=cv2.
                               INTER_CUBIC)
            image = image / 255
            pimages.append(image)
        pimages = np.array(pimages)
        image_shapes = np.array(shapes)
        return (pimages, image_shapes)

    def show_boxes(self, image, boxes, box_classes, box_scores, file_name):
        """ Show boxes"""
        for i, box in enumerate(boxes):
            x1 = int(box[0])
            y1 = int(box[1])
            start_point = int(box[0]), int(box[1])
            end_point = int(box[2]), int(box[3])
            scores = "{:.2f}".format(box_scores[i])
            label = (self.class_names[box_classes[i]] + " " + scores)
            oorg = (x1, y1 - 5)
            font = cv2.FONT_HERSHEY_SIMPLEX
            scale = 0.5
            text_color = (0, 0, 255)
            thick = 1
            line_Type = cv2.LINE_AA
            image = cv2.rectangle(image, start_point, end_point, (255, 0, 0),
                                  thickness=2)
            print(image)
            image = cv2.putText(image, label, oorg, font, scale, text_color,
                                thick, line_Type, bottomLeftOrigin=False)
        cv2.imshow(file_name, image)
        k = cv2.waitKey(0)
        if k == ord('s'):
            if not os.path.exists('detections'):
                os.makedirs('detections')
            os.chdir('detections')
            cv2.imwrite(file_name, image)
        cv2.destroyAllWindows()
