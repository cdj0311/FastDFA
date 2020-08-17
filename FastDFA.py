# encoding:utf-8
#############################################
# FileName: fast_dfa.py
# Author: ChenDajun
# CreateTime: 2020-08-17
# Descreption: DFA for text match
#############################################
import codecs


class cNode(object):
    """
    定义子节点
    """
    def __init__(self):
        self.children = None


class cDFA(object):
    """
    DFA(Deterministic Finite Automaton)的实现
    """
    def __init__(self, words_list=[]):
        self.root = None
        self.root = cNode()

        for w in words_list:
            self.add(w)

    def add(self, word):
        """ 将单词添加到状态机中 """
        node = self.root
        seq_len = len(word) - 1

        for i in range(len(word)):
            if not node.children:
                node.children = dict()
                if i != seq_len: node.children[word[i]] = (cNode(), False)
                else: node.children[word[i]] = (cNode(), True)
            elif word[i] not in node.children:
                if i != seq_len: node.children[word[i]] = (cNode(), False)
                else: node.children[word[i]] = (cNode(), True)
            else:
                if i == seq_len:
                    next_word, b_word = node.children[word[i]]
                    node.children[word[i]] = (next_word, True)
            node = node.children[word[i]][0]

    def search(self, text):
        """ 输入文本并搜索在词表中的词，并给出词在文本中的位置 """
        root = self.root
        seq_len = len(text)
        result = list()
        for i in range(seq_len):
            p, j = root, i
            while j < seq_len and p.children and text[j] in p.children:
                (p, b_word) = p.children[text[j]]
                if b_word: result.append([text[i:j+1], (i, j)])
                j = j + 1
        return result


if __name__ == "__main__":
    tree = cDFA([u"后长村", u"腾讯", u"新浪", u"百度"])
    tree.add(u"F4")
    tree.add(u"网易")
    tree.add(u"互联网")

    text = u"后长村的十字路口拥有号称F4的四大互联网公司，即：新浪，腾讯，百度，网易，外加一个联想."

    result = tree.search(text)
    for i in result:
        print(i)