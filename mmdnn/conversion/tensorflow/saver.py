import tensorflow as tf


def save_model(MainModel, network_filepath, weight_filepath, dump_filepath):
    input, model = MainModel.KitModel(weight_filepath)
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        saver = tf.train.Saver()
        save_path = saver.save(sess, dump_filepath)
        print('Tensorflow file is saved as [{}], generated by [{}.py] and [{}].'.format(
            save_path, network_filepath, weight_filepath))
