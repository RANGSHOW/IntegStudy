import tensorflow as tf

height = [170, 180, 175, 160]
shoe_size = [260, 270, 265, 255]

a = tf.Variable(0.1)
b = tf.Variable(0.2)

opt = tf.keras.optimizers.Adam(learning_rate=0.1) 
    # 경사하강법을 이용하여 변수 업데이트
    # learning_rate 없어도 알아서 할당함

def loss_func():
    pred = height * a + b
    return tf.square(260 - pred)  # 손실값 == (실제값 - 예측값)^2

for i in range(300):
    opt.minimize(loss_func, var_list=[a,b]) 
    print(a.numpy(), b.numpy())


# shoe_size = height * a + b
