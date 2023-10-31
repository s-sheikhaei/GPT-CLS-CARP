#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# NOTE: I cannot use a loop to go over the folds, because for each fold we need to take the best checkpoint, that I think is impossible to find it in this sh file.


PROJECT_PATH=/home/jovyan/SATD_Identification/CARP-Sun-2023/GPT-CLS-CARP
export PYTHONPATH="$PYTHONPATH:$PROJECT_PATH"


DATASET=OBrien
MODEL=gpt3_fewshot
STRATEGY=ft_retriever_knn
SETTING=carp

CONFIG_PATH="${PROJECT_PATH}/configs/${DATASET}/${MODEL}/${STRATEGY}/${SETTING}.json"

for fold in {0..9}
do
  for seed in 2333 # 8866 9998 6624 1314
  do
    echo "=============================================================================="
    echo "FOLD IS " ${fold}
    echo "SEED IS " ${seed}
    echo ${DATASET} "-" ${MODEL} "-" ${STRATEGY} "-" ${SETTING}
    echo "=============================================================================="

    # Replace "fold_X" with the current fold in the JSON file
    sed -i "s/fold_X/fold_${fold}/g" $CONFIG_PATH

    python3 ${PROJECT_PATH}/task/gpt3_text_cls.py \
    --seed ${seed} --random \
    --config_path $CONFIG_PATH \
    --step_idx 1-2-3-4

    # Revert the changes in the JSON file
    sed -i "s/fold_${fold}/fold_X/g" $CONFIG_PATH
  done
done
