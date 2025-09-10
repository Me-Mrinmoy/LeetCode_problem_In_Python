class Solution {
public:
    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> res;
        while(head){
            res.push_back(head->val);
            head = head->next;
        }
        stack<int> st;
        for(int i = res.size() - 1; i >= 0; --i){
            while(!st.empty() && st.top() <= res[i]) st.pop();
            int temp = (st.empty()) ? 0 : st.top();
            st.push(res[i]);
            res[i] = temp;
        }
        return res;
    }
};
