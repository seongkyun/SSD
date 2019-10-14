import os

class DatasetCatalog:
    #DATA_DIR = 'datasets'
    DATA_DIR = '/mnt/hdd640'
    DATASETS = {
        'custom_train': {
            "data_dir": "NOTA/Face_data_split",
            "split": "trainval"
        },
        'custom_test': {
            "data_dir": "NOTA/Face_data_split",
            "split": "test"
        },
        'voc_2007_train': {
            "data_dir": "VOCdevkit/VOC2007",
            "split": "train"
        },
        'voc_2007_val': {
            "data_dir": "VOCdevkit/VOC2007",
            "split": "val"
        },
        'voc_2007_trainval': {
            "data_dir": "VOCdevkit/VOC2007",
            "split": "trainval"
        },
        'voc_2007_test': {
            "data_dir": "VOCdevkit/VOC2007",
            "split": "test"
        },
        'voc_2012_train': {
            "data_dir": "VOCdevkit/VOC2012",
            "split": "train"
        },
        'voc_2012_val': {
            "data_dir": "VOCdevkit/VOC2012",
            "split": "val"
        },
        'voc_2012_trainval': {
            "data_dir": "VOCdevkit/VOC2012",
            "split": "trainval"
        },
        'voc_2012_test': {
            "data_dir": "VOCdevkit/VOC2012",
            "split": "test"
        },
        'coco_2014_valminusminival': {
            "data_dir": "val2014",
            "ann_file": "annotations/instances_valminusminival2014.json"
        },
        'coco_2014_minival': {
            "data_dir": "val2014",
            "ann_file": "annotations/instances_minival2014.json"
        },
        'coco_2014_train': {
            "data_dir": "train2014",
            "ann_file": "annotations/instances_train2014.json"
        },
        'coco_2014_val': {
            "data_dir": "val2014",
            "ann_file": "annotations/instances_val2014.json"
        },
    }

    @staticmethod
    def get(name):
        if "voc" in name:
            voc_root = DatasetCatalog.DATA_DIR
            if 'VOC_ROOT' in os.environ:
                voc_root = os.environ['VOC_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(voc_root, attrs["data_dir"]),
                split=attrs["split"],
            )
            print(os.path.join(voc_root, attrs["data_dir"]))
            return dict(factory="VOCDataset", args=args)
        elif "coco" in name:
            coco_root = DatasetCatalog.DATA_DIR
            if 'COCO_ROOT' in os.environ:
                coco_root = os.environ['COCO_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(coco_root, attrs["data_dir"]),
                ann_file=os.path.join(coco_root, attrs["ann_file"]),
            )
            return dict(factory="COCODataset", args=args)
        elif "custom" in name:
            custom_root = DatasetCatalog.DATA_DIR
            if 'VOC_ROOT' in os.environ:
                custom_root = os.environ['VOC_ROOT']

            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                data_dir=os.path.join(custom_root, attrs["data_dir"]),
                split=attrs["split"],
            )
            print(os.path.join(custom_root, attrs["data_dir"]))
            return dict(factory="CustomDataset", args=args)

        raise RuntimeError("Dataset not available: {}".format(name))
