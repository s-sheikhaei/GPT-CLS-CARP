#!/usr/bin/env bash
# -*- coding: utf-8 -*-

PROJECT_PATH=/home/jovyan/SATD_Identification/CARP-Sun-2023/GPT-CLS-CARP
export PYTHONPATH="$PYTHONPATH:$PROJECT_PATH"


# BERT_PATH='bert-base-uncased'
BERT_PATH='roberta-large'
# BERT_PATH=/data2/lixiaoya/models/roberta-large

# FILE_NAME=obrien_bert_base
FILE_NAME=obrien_roberta_large
SAVE_TOPK=20
DATA_DIR=/home/jovyan/SATD_Identification/CARP-Sun-2023/data/obrien/fold_0

DATA_SIGN=obrien

WEIGHT_DECAY=0.05
WARMUP_PROPORTION=0.06
MAX_LEN=512
MAX_EPOCH=8
DROPOUT=0.2
ACC_GRAD=1
VAL_CHECK_INTERVAL=1.0


# 目前使用一张GPU，precision==16 或者 precision==32可以得到相同的结果。

for TRAIN_BATCH_SIZE in 16
do
  for LR in 2e-5 # 1e-5 3e-5 2e-5 4e-5
  do

    OUTPUT_DIR=/home/jovyan/SATD_Identification/CARP-Sun-2023/outputs/trained_models/${FILE_NAME}/epoch${MAX_EPOCH}_bs${TRAIN_BATCH_SIZE}_lr${LR}_weightdecay${WEIGHT_DECAY}_warmup${WARMUP_PROPORTION}_maxlen${MAX_LEN}_dropout${DROPOUT}_grad${ACC_GRAD}
    mkdir -p ${OUTPUT_DIR}
    mkdir -p ${OUTPUT_DIR}/checkpoint

    echo ${OUTPUT_DIR}

    echo "==============================================================="
    cp ${PROJECT_PATH}/script/${DATA_SIGN}/finetune_roberta_large.sh ${OUTPUT_DIR}
    echo "==============================================================="

    CUDA_VISIBLE_DEVICES=0 python3 ${PROJECT_PATH}/task/finetune_mlm_text_cls.py \
    --lr ${LR} \
    --max_epochs ${MAX_EPOCH} \
    --max_length ${MAX_LEN} \
    --weight_decay ${WEIGHT_DECAY} \
    --hidden_dropout_prob ${DROPOUT} \
    --warmup_proportion ${WARMUP_PROPORTION} \
    --batch_size ${TRAIN_BATCH_SIZE} \
    --accumulate_grad_batches ${ACC_GRAD} \
    --save_topk ${SAVE_TOPK} \
    --bert_path ${BERT_PATH} \
    --data_dir ${DATA_DIR} \
    --dataset_name ${DATA_SIGN} \
    --save_path ${OUTPUT_DIR} \
    --val_check_interval ${VAL_CHECK_INTERVAL} \
    --gpus="1" \
    --precision=16
    done
done

#--only_eval \
#    --eval_ckpt_path /data2/lixiaoya/outputs/gpt-text/sst2_fix/sst2_roberta_large/epoch5_bs32_lr3e-5_weightdecay0.1_warmup0.06_maxlen200_dropout0.2_grad1/checkpoint/epoch=2-val_loss=0.2398-val_acc=0.9667.ckpt
#


