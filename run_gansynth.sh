# python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir --batch_size $1

#############################

# # 10
# for i in 1 2 3 4 5
# do
#   python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_10_$i --batch_size 10
# done
#
# # 20
# for i in 1 2 3 4 5
# do
#   python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_20_$i --batch_size 20
# done
#
# # 30
# for i in 1 2 3 4 5
# do
#   python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_30_$i --batch_size 30
# done
#
# # 40
# for i in 1 2 3 4 5
# do
#   python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_40_$i --batch_size 40
# done
#
# # 50
# for i in 1 2 3 4 5
# do
#   python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_50_$i --batch_size 50
# done

###############################

# 60
for i in 1 2 3 4 5
do
  python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_60_$i --batch_size 60
done

# 70
for i in 1 2 3 4 5
do
  python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_70_$i --batch_size 70
done

# 80
for i in 1 2 3 4 5
do
  python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_80_$i --batch_size 80
done

# 90
for i in 1 2 3 4 5
do
  python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_90_$i --batch_size 90
done

# 100
for i in 1 2 3 4 5
do
  python magenta/models/gansynth/gansynth_generate.py --ckpt_dir=magenta/models/gansynth/acoustic_only --output_dir=magenta/models/gansynth/output_dir_100_$i --batch_size 100
done
