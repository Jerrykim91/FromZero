<br>

# Transfer Learnning : 전이 학습
<br>

Transfer Learnning의 장점
- 기본적인 성능 향상
- 전반적인 모델 개발 및 훈련 시간 단축, 그리고 우수한 모델


```py

BATCH_SIZE = 64
EPOCHS = 100
NUM_CLASSES = 4
LEARNING_RATE = 1e-4
MOMENTUM = 0.9
PATH="C:\FoodClassification\data"
```

```py
base_model = vgg.VGG16(weights='imagenet', 
                       include_top=False, 
                       input_shape=(128, 128, 3))


# VGG16 모델의 세 번째 블록에서 마지막 층 추출
last = base_model.get_layer('block3_pool').output

```