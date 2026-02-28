#include <bits/stdc++.h>
using namespace std;

const int M = 1'000'000'007;
const int X = 101113;

struct SegmentTree {
    int size;
    vector<int> val_tree, hash_tree, length_tree;
    vector<long long> x, h;

    SegmentTree(int n, const vector<int>& nums) {
        int k = 1;
        while (k < n) k <<= 1;
        size = k;

        val_tree.assign(k * 2 - 1, 0);
        hash_tree.assign(k * 2 - 1, 0);
        length_tree.assign(k * 2 - 1, 1);

        x.assign(n + 1, 1);
        h.assign(n + 1, 0);

        for (int i = 1; i <= n; ++i) {
            x[i] = x[i - 1] * X % M;
            h[i] = (h[i - 1] + x[i - 1]) % M;
        }

        for (int i = 0; i < n; ++i) {
            hash_tree[k - 1 + i] = nums[i];
        }

        for (int i = k - 2; i >= 0; --i) {
            int len = length_tree[i * 2 + 1];
            length_tree[i] = len * 2;
            hash_tree[i] = (1LL * hash_tree[i * 2 + 1] * x[len] + hash_tree[i * 2 + 2]) % M;
        }
    }

    void assign(int l, int r, int val) {
        traversal(0, l, r, val, 0, size);
    }

    bool compare(int l1, int l2, int length) {
        auto [len_l, hash_l] = traversal(0, l1, l1 + length, 0, 0, size);
        auto [len_r, hash_r] = traversal(0, l2, l2 + length, 0, 0, size);
        return hash_l == hash_r;
    }

    pair<int, long long> traversal(int i, int l, int r, int val, int cur_l, int cur_r) {
        if (cur_r <= l || cur_l >= r) {
            if (val_tree[i]) {
                hash_tree[i] = 1LL * val_tree[i] * h[length_tree[i]] % M;
            }
            return {0, hash_tree[i]};
        }

        if (l <= cur_l && cur_r <= r) {
            if (val) val_tree[i] = val;
            if (val_tree[i]) {
                hash_tree[i] = 1LL * val_tree[i] * h[length_tree[i]] % M;
            }
            return {length_tree[i], hash_tree[i]};
        }

        if (val_tree[i]) {
            val_tree[i * 2 + 1] = val_tree[i];
            val_tree[i * 2 + 2] = val_tree[i];
            val_tree[i] = 0;
        }

        auto [len_l, hash_l] = traversal(i * 2 + 1, l, r, val, cur_l, (cur_l + cur_r) / 2);
        auto [len_r, hash_r] = traversal(i * 2 + 2, l, r, val, (cur_l + cur_r) / 2, cur_r);

        hash_tree[i] = (1LL * hash_tree[i * 2 + 1] * x[length_tree[i] / 2] + hash_tree[i * 2 + 2]) % M;

        long long combined = ((len_l ? hash_l * x[len_r] : 0) + (len_r ? hash_r : 0)) % M;
        return {len_l + len_r, combined};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> nums(n);
    for (int& x : nums) cin >> x;

    SegmentTree tree(n, nums);

    int m;
    cin >> m;
    string result;
    while (m--) {
        int t, l, r, k;
        cin >> t >> l >> r >> k;
        if (t == 0) {
            tree.assign(l - 1, r, k);
        } else {
            result += (l == r || tree.compare(l - 1, r - 1, k)) ? '+' : '-';
        }
    }
    cout << result << '\n';
    return 0;
}
