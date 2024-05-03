import tensorflow as tf

def test_ok_1():
    with open('def.txt', 'w'):
        pass

def test_ok_2():
    @tf.function
    def append_to_list(x):
        return x * x

    # Testing the monkey-patched tf.function
    print(append_to_list(tf.constant(2)))
    print(append_to_list(tf.constant(3)))
    print(append_to_list(tf.constant(2.0)))

def test_violation_1():
    @tf.function
    def append_to_list(x):
        with open('abc.txt', 'w'):
            pass
        return x * x

    # Testing the monkey-patched tf.function
    print(append_to_list(tf.constant(2)))