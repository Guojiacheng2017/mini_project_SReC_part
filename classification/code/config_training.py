config = {
    'data_path': '../dataset',
    'test_data_path': '/mnt/SReC/decomp_waste_test', # '../dataset_test'
    'model_path': '../model/res18_epoch', ##### '../model/res18_epoch', '../model/wasteCNN_epoch', '../model/CNN_epoch'
    # 'preprocess_result_path': '',
    'image_size': 128,  # 256
    'batch_size': 32,
#     'test_percentage': 0.2,
    'val_percentage': 0.2,
    'lr': 1e-3,
    'epoch': 50,
    'classifier_model': 'model',
#     'classifier_param': "../model/classifier.ckpt",
#     'skip_preprocessing': True
}

