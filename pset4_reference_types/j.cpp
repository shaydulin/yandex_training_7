#include <fstream>
#include <iostream>
#include <vector>
#include <memory>
using namespace std;

struct Node {
    int cnt = 0;
    long long square_sum = 0;
    shared_ptr<Node> left = nullptr;
    shared_ptr<Node> right = nullptr;
    int first = -1;
    int last = -1;
    bool to_remove = false;
};

shared_ptr<Node> create_node(int left_bound, int right_bound) {
    auto node = make_shared<Node>();
    if (left_bound == right_bound) {
        node->first = node->last = right_bound;
    }
    return node;
}

class SegmentTree {
public:
    SegmentTree(const vector<int>& arr) {
        right_bound = 0;
        for (int x : arr) right_bound += x;
        root = create_node(0, right_bound);
        vector<int> tmp = arr;
        tmp.push_back(-1); // for safety
        int i = 0;
        build(root, tmp, i, 0, 0, right_bound);
    }

    long long divide_and_join(int v) {
        auto [left_border, middle, right_border] = traversal(v, root);
        if (left_border != 0 && right_border != right_bound)
            add(root, middle, 0, right_bound);
        if (left_border != 0)
            remove(root, left_border, 0, right_bound);
        if (right_border != right_bound)
            remove(root, right_border, 0, right_bound);
        return root->square_sum;
    }

    long long divide(int v) {
        auto [left_border, middle, right_border] = traversal(v, root);
        add(root, middle, 0, right_bound);
        return root->square_sum;
    }

    shared_ptr<Node> root;

private:
    int right_bound;

    int build(shared_ptr<Node> node, const vector<int>& arr, int& i, int cur_val, int left_bound, int right_bound) {
        if (left_bound == right_bound) {
            if (i >= arr.size()) return -1;
            return cur_val + arr[i++];
        }

        int middle = (left_bound + right_bound) >> 1;
        while (i < arr.size() && cur_val <= right_bound) {
            if (cur_val <= middle) {
                if (!node->left)
                    node->left = create_node(left_bound, middle);
                cur_val = build(node->left, arr, i, cur_val, left_bound, middle);
            } else {
                if (!node->right)
                    node->right = create_node(middle + 1, right_bound);
                cur_val = build(node->right, arr, i, cur_val, middle + 1, right_bound);
            }
        }
        update(node);
        return cur_val;
    }

    tuple<int, int, int> traversal(int v, shared_ptr<Node> node) {
        int cnt_l = node->left ? node->left->cnt : 0;
        int cnt_r = node->right ? node->right->cnt : 0;
        if (cnt_l >= v) {
            return traversal(v, node->left);
        } else if (cnt_l == v - 1 && node->cnt - cnt_l - cnt_r != 0) {
            return {node->left->last, (node->left->last + node->right->first) >> 1, node->right->first};
        } else {
            v -= cnt_l;
            if (node->cnt - cnt_l - cnt_r != 0)
                v -= 1;
            return traversal(v, node->right);
        }
    }

    void remove(shared_ptr<Node>& node, int border, int left_bound, int right_bound) {
        int middle = (left_bound + right_bound) >> 1;
        if (border <= middle) {
            if (middle - left_bound > 0) {
                remove(node->left, border, left_bound, middle);
                if (node->left && node->left->to_remove)
                    node->left = nullptr;
            } else {
                node->left = nullptr;
            }
        } else {
            if (right_bound - middle - 1 > 0) {
                remove(node->right, border, middle + 1, right_bound);
                if (node->right && node->right->to_remove)
                    node->right = nullptr;
            } else {
                node->right = nullptr;
            }
        }
        if (!node->left && !node->right) {
            node->to_remove = true;
        } else {
            update(node);
        }
    }

    void add(shared_ptr<Node>& node, int border, int left_bound, int right_bound) {
        int middle = (left_bound + right_bound) >> 1;
        if (border <= middle) {
            if (!node->left)
                node->left = create_node(left_bound, middle);
            if (middle - left_bound > 0)
                add(node->left, border, left_bound, middle);
        } else {
            if (!node->right)
                node->right = create_node(middle + 1, right_bound);
            if (right_bound - middle - 1 > 0)
                add(node->right, border, middle + 1, right_bound);
        }
        update(node);
    }

    void update(shared_ptr<Node>& node) {
        auto& l = node->left;
        auto& r = node->right;
        int last_left = -1, first_right = -1;
        node->cnt = 0;
        node->square_sum = 0;
        if (l) {
            node->cnt += l->cnt;
            node->square_sum += l->square_sum;
            node->first = l->first;
            last_left = l->last;
            if (!r) node->last = l->last;
        }
        if (r) {
            node->cnt += r->cnt;
            node->square_sum += r->square_sum;
            node->last = r->last;
            first_right = r->first;
            if (!l) node->first = r->first;
        }
        if (last_left != -1 && first_right != -1) {
            node->cnt += 1;
            long long diff = first_right - last_left;
            node->square_sum += diff * diff;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int n;
    fin >> n;
    vector<int> a(n);
    for (int& x : a) fin >> x;

    SegmentTree tree(a);
    fout << tree.root->square_sum << '\n';

    int k;
    fin >> k;
    for (int i = 0; i < k; ++i) {
        int typ, v;
        fin >> typ >> v;
        if (typ == 1)
            fout << tree.divide_and_join(v) << '\n';
        else
            fout << tree.divide(v) << '\n';
    }
    return 0;
}
