from zhlib import zh

from zhsentence.util import get_freq, zh_split

all_entries = list()

for vocab in zh_split('''
打扮，不满，世界
避孕，辟邪，长得，贴
小蜜，怀孕，老婆，打闹，跑掉，上司
被人，利用
紧张，填，岳母，栏目，挺好
连，广告
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
