from zhlib import zh

from zhsentence.util import get_freq, zh_split

all_entries = list()

for vocab in zh_split('''
课堂，沉睡，酒桌，埋醉
一斤，感觉，绝对
实行，凭什么，平等，厕所

客服人员，权，答这答那
实现，承诺，艹你妈
'''):
    entry = [''] * 7
    entry[1] = vocab
    entry[6] = str(round(get_freq(vocab), 3))

    results = zh.Vocab.match(vocab)
    if len(results) > 0:
        entry[0] = '，'.join(r.english for r in results if r.english)
        entry[2] = '，'.join(r.traditional for r in results if r.traditional and r.traditional != vocab)
        entry[3] = '，'.join(r.pinyin for r in results if r.pinyin)

    all_entries.append(entry)

# all_entries = sorted(all_entries, key=lambda x: -float(x[6]))

print('\n'.join('\t'.join(e) for e in all_entries))
