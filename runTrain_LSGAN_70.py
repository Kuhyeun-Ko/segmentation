import os

os.system("python3 segment_LSGAN_70.py train -d datasets/cityscapes/gtFine_trainvaltest -c 19 -s 512 \
    --arch drn_c_26 --batch-size 25 --epochs 250 --lr 0.01 --momentum 0.9 \
    --step 100");
