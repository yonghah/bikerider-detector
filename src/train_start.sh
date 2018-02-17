# move to your tensorflow object detection directory
cd ~/repo/tensorflow/models/research
# change parameters accordingly
python object_detection/train.py \
--logtostderr \
--pipeline_config_path=/home/ubuntu/repo/bike-detector/data/training/config/faster_rcnn_resnet101_coco.config \
--train_dir=/home/ubuntu/repo/bike-detector/data/training/train
