from multiprocessing.pool import Pool
import math

def mutli_processing(batch_size, datas,  process_func, handle_reuslt_function = None, start_batch_index = 0):
    cnt = len(datas)
    batch_cnt = math.ceil(cnt / batch_size)

    print('-------> start multi processing')

    if start_batch_index >= batch_cnt:
        print('start batch index exceed the total batch count')
        return

    for idx in range(start_batch_index, batch_cnt+1):
        start_idx = batch_size * idx
        end_idx = min(cnt, batch_size * (idx + 1))
        batch_data = datas[start_idx: end_idx]

        with Pool() as pool:
            results = pool.map(process_func, batch_data)
            if handle_reuslt_function is not None:
                handle_reuslt_function(results)

    print('-------> end multi processing')