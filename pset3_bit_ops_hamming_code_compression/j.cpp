#include <bits/stdc++.h>
using namespace std;

const int BITS = 8;
unordered_map<char, int> idxs_of_letters;
unordered_map<int, char> letters_by_idcs;

struct Node {
    int id;
    unordered_map<char, int> next;
};

vector<Node> trie;
vector<string> WORDS;

void init() {
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    for (int i = 0; i < alphabet.size(); i++) {
        idxs_of_letters[alphabet[i]] = i;
        letters_by_idcs[i] = alphabet[i];
    }
    trie.push_back({0, {}});
    WORDS.push_back("");
}

vector<int> pack(const string &s) {
    int cur = 0;
    long long bit_sequence = 1;
    int prev_word_idx_bits = 1;

    for (char ch : s) {
        if (trie[cur].next.count(ch)) {
            cur = trie[cur].next[ch];
        } else {
            bit_sequence <<= prev_word_idx_bits;
            bit_sequence |= trie[cur].id;
            bit_sequence <<= 5;
            bit_sequence |= idxs_of_letters[ch];

            trie[cur].next[ch] = trie.size();
            trie.push_back({(int)WORDS.size(), {}});
            WORDS.push_back(WORDS[trie[cur].id] + ch);

            if (WORDS.size() == (1 << prev_word_idx_bits)) prev_word_idx_bits++;
            cur = 0;
        }
    }

    if (cur != 0) {
        bit_sequence <<= prev_word_idx_bits;
        bit_sequence |= trie[cur].id;
    }

    bit_sequence <<= 1;
    bit_sequence |= 1;

    vector<int> res;
    while (bit_sequence) {
        res.push_back(bit_sequence & ((1 << BITS) - 1));
        bit_sequence >>= BITS;
    }

    return res;
}

string unpack(const vector<int> &chunks) {
    long long bit_sequence = 0;
    for (int i = chunks.size() - 1; i >= 0; i--) {
        bit_sequence <<= BITS;
        bit_sequence |= chunks[i];
    }

    bit_sequence >>= 1;
    int prev_word_idx_bits = 1;
    int letter_bits = 5;
    int letter_mask = (1 << letter_bits) - 1;
    string res;

    while (bit_sequence > 0) {
        int prev_word_idx = bit_sequence & ((1 << prev_word_idx_bits) - 1);
        res += WORDS[prev_word_idx];
        bit_sequence >>= prev_word_idx_bits;

        if (bit_sequence == 0) break;
        int letter_idx = bit_sequence & letter_mask;
        res += letters_by_idcs[letter_idx];
        bit_sequence >>= letter_bits;

        WORDS.push_back(WORDS[prev_word_idx] + letters_by_idcs[letter_idx]);

        if (WORDS.size() == (1 << prev_word_idx_bits)) prev_word_idx_bits++;
    }

    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    init();
    string op;
    cin >> op;

    if (op == "pack") {
        string s;
        cin >> s;
        vector<int> res = pack(s);
        cout << res.size() << "\n";
        for (int x : res) {
            cout << x << " ";
        }
        cout << "\n";
    } else {
        int n;
        cin >> n;
        vector<int> chunks(n);
        for (int i = 0; i < n; i++) {
            cin >> chunks[i];
        }
        cout << unpack(chunks) << "\n";
    }

    return 0;
}
