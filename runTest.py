import os


# os.system('python3 segment.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
#      --pretrained checkpoints/drn/model_best.pth.tar --phase val --batch-size 1 ')

# os.system('python3 segment_LSGAN_1.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
#      --pretrained checkpoints/drn_LSGAN_1/model_best.pth.tar --phase val --batch-size 1 > ./mIOU/LSGAN_1.txt')

# os.system('python3 segment_LSGAN_70.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
#      --pretrained checkpoints/drn_LSGAN_70/model_best.pth.tar --phase val --batch-size 1 > ./mIOU/LSGAN_70.txt')

# os.system('python3 segment_LSGAN_142.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
#      --pretrained checkpoints/drn_LSGAN_142/model_best.pth.tar --phase val --batch-size 1 > ./mIOU/LSGAN_142.txt')

# os.system('python3 segment_LSGAN_238.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
#      --pretrained checkpoints/drn_LSGAN_238/model_best.pth.tar --phase val --batch-size 1 > ./mIOU/LSGAN_238.txt')

#      --pretrained checkpoints/drn_LSGAN_430/model_best.pth.tar --phase val --batch-size 1 > ./mIOU/LSGAN_430.txt')
# os.system('python3 segment_LSGAN_430.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\

# os.system('python3 segment_LSGAN_1.py test -d ./dataset/cityscapes/ -c 19 --arch drn_c_26\
#      --pretrained checkpoints/drn_LSGAN_1/model_best.pth.tar --phase val --batch-size 1 ')

# os.system('python3 segment.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26 \
#     --pretrained checkpoints/drn_LSGAN_430/model_best.pth.tar --phase test --batch-size 1')



# os.system('python3 segment.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
#      --pretrained checkpoints/drn/model_best.pth.tar --phase val --batch-size 1 ')

os.system('python3 segment_WGAN_1.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
     --pretrained checkpoints/drn_WGAN_1/model_best.pth.tar --phase val --batch-size 1 ')

os.system('python3 segment_WGAN_70.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
     --pretrained checkpoints/drn_WGAN_70/model_best.pth.tar --phase val --batch-size 1 ')

os.system('python3 segment_WGAN_142.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
     --pretrained checkpoints/drn_WGAN_142/model_best.pth.tar --phase val --batch-size 1 ')

os.system('python3 segment_WGAN_238.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
     --pretrained checkpoints/drn_WGAN_238/model_best.pth.tar --phase val --batch-size 1 ')

os.system('python3 segment_WGAN_430.py test -d datasets/cityscapes/gtFine_trainvaltest -c 19 --arch drn_c_26\
   --pretrained checkpoints/drn_WGAN_430/model_best.pth.tar --phase val --batch-size 1 ')
# os.system('python3 segment_LSGAN_1.py test -d ./dataset/cityscapes/ -c 19 --arch drn_c_26\
     # --pretrained checkpoints/drn_LSGAN_1/model_best.pth.tar --phase val --batch-size 1 ')
# 
