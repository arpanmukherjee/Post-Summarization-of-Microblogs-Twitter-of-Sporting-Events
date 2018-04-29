###############################################################################
#
##
## tweetToOriginal - map obatined tweets to original tweets
#
import csv

inOrig = '/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/originalData/TW_INDSA_13feb.csv'
inMapper = '/media/adalove/WorkDrive/M.Tech/Sem2/IR/project/project_IR/Post-Summarization-of-Microblogs-Twitter-of-Sporting-Events/Dataset/cleanedData/mapper.csv'
def getMapper():
    mapper = []
    with open(inMapper, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            mapper.append(row[1])
    return mapper

def getOriginal():
    orig={}
    with open(inOrig, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            orig[row[2]] = row[1]
    return orig

def getOriginalTweets(tweets):
    orig = getOriginal()
    mapper = getMapper()
    new_tweets = []

    for t in tweets:
        #print t
        if str(t) in mapper:

            id = str(mapper.index(str(t)) + 1)
            new_tweets.append(orig[id])


    return new_tweets


# tweets = [[u'score', u'4', u'run', u'death', u'over', u'odi', u'noth', u'less', u'crime', u'bcci', u'middl', u'order', u'master', u'thi\u2026'],
# [u'agre', u'hardik', u'pandya', u'kick', u'next', u'match', u'93', u'run', u'sa', u'tour..', u'savind', u'indvsa', u'rohit', u'sharma', u'dhoni'],
# [u'dear', u'virat', u'imvkohli', u'msdhoni', u'ko', u'7', u'pe', u'bhi', u'kyu', u'bhejt', u'ho', u'11', u'bheja', u'karo', u'na\U0001f611\U0001f61f\u2026', u'http', u'//t.co/ciza4qfoij'],
# [u'cricketnext', u'imro45', u'help', u'...', u'\U0001f602\U0001f602\U0001f602\U0001f602\U0001f602', u'u', u'r', u'involv', u'2', u'run', u'outs..', u'suppos', u'there\u2026'],
# [u'watch', u'imro45', u'score', u'\U0001f4af', u'realli', u'one', u'best', u'feel', u'one', u'best', u'\U0001f4af', u'pressur', u'indvsa', u'teamindia.\u2026'],
# [u'savind', u'dhoni', u'bhuvi', u'best', u'finish', u'day'],
# [u'innings_break', u'sa_vs_ind', u'5th_odi', u'ind_274/7', u'ovr_50', u'b', u'kumar_19*', u'20b', u'2x4', u'0x6', u'kuldeep_2*', u'4b', u'0x4', u'0x6', u'k', u'rabada', u'1-1\u2026'],
# [u'savind', u'ridicul', u'captainci', u'virat', u'send', u'suresh', u'hardik', u'dhoni'],
# [u'bcci', u'hardikpandya7', u'hardik', u'pandya', u'must', u'everi', u'thing', u'sa', u'play', u'cricket', u'savind'],
# [u'time', u'2019', u'world', u'cup', u'begin', u'dhoni', u'would', u'reduc', u'excel', u'keeper', u'bat', u'bit', u'savind'],
# [u'55/4', u'teamindia', u'last', u'10', u'overs..', u'sa', u'seal', u'match..', u'hope', u'think', u'so..', u'the\u2026'],
# [u'actual', u"'s", u'neither', u'bhuvi', u'pandya', u'rounder', u'match', u'got', u'ta', u'rohit', u'sharma', u'centuri', u'amp', u'2\u2026'],
# [u'mohansharma51', u'big', u'ton', u'due', u'imro45', u'patienc', u'virtu', u'indvsa'],
# [u'india', u'might', u'20-30', u'run', u'short', u'run', u'out', u'savind'],
# [u'time', u'spectat', u'show', u'skill', u'indvsa', u"n't", u'u', u'allow', u'bcci'],
# [u'bhubaneswar', u'kumar', u'start', u'play', u'better', u'u', u'someth', u'wrong', u'dhoni', u'indvsa'],
# [u'savind', u'someon', u'remind', u'hardik', u'pandya', u'tour', u'south', u'africa', u'play', u'cricket', u'color', u'blue', u'blond', u'hair', u'danc'],
# [u'kohli', u'pandya', u'rahan', u'iyer', u'play', u'slowli', u'blame', u'dhoni', u'low', u'score', u"'s", u'the\u2026'],
# [u'time', u'bring', u'rishabpant777', u'middl', u'order', u'indvsa']]

# tweets = [[u'yemen', u'80', u'popul', u'need', u'aid', u'surviv', u'yemencantwait', u'yemenneglect', u'soompiaward', u'sblii\u2026'],
# [u'deliv', u'flyeaglesfli', u'eagl', u'superbowlchamp'],
# [u'``', u"'m", u'go', u'white', u'hous', u'kid', u"''", u'said', u'eagl', u'defens', u'end', u'chri', u'long', u'also', u'skipped\u2026'],
# [u'amount', u'babi', u'conceiv', u'last', u'night', u'philadelphia', u'probabl', u'outnumb', u'babi', u'conceiv', u'baby\u2026']]


tweets =[[u'score', u'4', u'run', u'death', u'over', u'odi', u'noth', u'less', u'crime', u'bcci', u'middl', u'order', u'master', u'thi\u2026'],
[u'agre', u'hardik', u'pandya', u'kick', u'next', u'match', u'93', u'run', u'sa', u'tour..', u'savind', u'indvsa', u'rohit', u'sharma', u'dhoni'],
[u'dear', u'virat', u'imvkohli', u'msdhoni', u'ko', u'7', u'pe', u'bhi', u'kyu', u'bhejt', u'ho', u'11', u'bheja', u'karo', u'na\U0001f611\U0001f61f\u2026', u'http', u'//t.co/ciza4qfoij'],
[u'cricketnext', u'imro45', u'help', u'...', u'\U0001f602\U0001f602\U0001f602\U0001f602\U0001f602', u'u', u'r', u'involv', u'2', u'run', u'outs..', u'suppos', u'there\u2026'],
[u'watch', u'imro45', u'score', u'\U0001f4af', u'realli', u'one', u'best', u'feel', u'one', u'best', u'\U0001f4af', u'pressur', u'indvsa', u'teamindia.\u2026'],
[u'savind', u'dhoni', u'bhuvi', u'best', u'finish', u'day'],
[u'innings_break', u'sa_vs_ind', u'5th_odi', u'ind_274/7', u'ovr_50', u'b', u'kumar_19*', u'20b', u'2x4', u'0x6', u'kuldeep_2*', u'4b', u'0x4', u'0x6', u'k', u'rabada', u'1-1\u2026'],
[u'savind', u'ridicul', u'captainci', u'virat', u'send', u'suresh', u'hardik', u'dhoni'],
[u'bcci', u'hardikpandya7', u'hardik', u'pandya', u'must', u'everi', u'thing', u'sa', u'play', u'cricket', u'savind'],
[u'time', u'2019', u'world', u'cup', u'begin', u'dhoni', u'would', u'reduc', u'excel', u'keeper', u'bat', u'bit', u'savind'],
[u'55/4', u'teamindia', u'last', u'10', u'overs..', u'sa', u'seal', u'match..', u'hope', u'think', u'so..', u'the\u2026'],
[u'actual', u"'s", u'neither', u'bhuvi', u'pandya', u'rounder', u'match', u'got', u'ta', u'rohit', u'sharma', u'centuri', u'amp', u'2\u2026'],
[u'mohansharma51', u'big', u'ton', u'due', u'imro45', u'patienc', u'virtu', u'indvsa'],
[u'india', u'might', u'20-30', u'run', u'short', u'run', u'out', u'savind'],
[u'time', u'spectat', u'show', u'skill', u'indvsa', u"n't", u'u', u'allow', u'bcci'],
[u'bhubaneswar', u'kumar', u'start', u'play', u'better', u'u', u'someth', u'wrong', u'dhoni', u'indvsa'],
[u'savind', u'someon', u'remind', u'hardik', u'pandya', u'tour', u'south', u'africa', u'play', u'cricket', u'color', u'blue', u'blond', u'hair', u'danc'],
[u'kohli', u'pandya', u'rahan', u'iyer', u'play', u'slowli', u'blame', u'dhoni', u'low', u'score', u"'s", u'the\u2026'],
[u'time', u'bring', u'rishabpant777', u'middl', u'order', u'indvsa'],
[u'indvsa', u'\u0930\u094b\u0939\u093f\u0924', u'\u0936\u0930\u094d\u092e\u093e', u'\u0915\u093e', u'\u0927\u092e\u093e\u0915\u093e', u'\u0926\u0915\u094d\u0937\u093f\u0923', u'\u0905\u092b\u094d\u0930\u0940\u0915\u093e', u'\u0915\u0947', u'\u0916\u093f\u0932\u093e\u092b', u'\u0920\u094b\u0915\u093e', u'\u0905\u092a\u0928\u093e', u'17\u0935\u093e\u0902', u'\u0935\u0928\u0921\u0947', u'\u0936\u0924\u0915', u'http', u'//t.co/pzrr0qfspv']]

nt = getOriginalTweets(tweets)
print nt
for k in nt:
    t = k.split(" ")
    for tt in t:
        print tt.decode('utf-8'),
    print
    #print('___________________________________________________________________________________')

