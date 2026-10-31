// for this problem, I used C++.
// (ALGO) CHECK VERTICAL ALIGNMENT (EASY). THEN CHECK_DIAGONALS()
// CHECK DIAGONALS(): ABS(X1-X2) != ABS(Y1-Y2) FOR ALL TUPLES (X1,Y1) != (X2,Y2) :)

#include <algorithm>
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<int>> possible_sols;
        vector<vector<int>> master_list;
        for (int i=0;i<n;i++){
            vector<int> taken_cols{};
            master_list.emplace_back(taken_cols);
            solveNQueensReq(n, possible_sols, taken_cols, i);
        }
        vector<vector<string>> possible_strings;
        for (vector<int> sol: possible_sols){
            vector<string> string_sol;
            for(int i: sol){
            string character(".");
            string result;
            result.assign(n,character[0]);
            result[i]='Q';
            string_sol.push_back(result);
        }
        possible_strings.push_back(string_sol);
        }
        return possible_strings;
    }
    void solveNQueensReq(int n,vector<vector<int>>& possible_sols, vector<int>& taken_cols, int num){
        taken_cols.push_back(num);

         if(taken_cols.size()== n){
             possible_sols.push_back(taken_cols);
             return;
         }
        vector<vector<int>> copies;
        for (int i=0;i<n;i++){
            if(check_comp(taken_cols, i)){
            vector<int> copy= taken_cols;
            copies.emplace_back(copy);
            solveNQueensReq(n, possible_sols, copy, i);
            }


        }
    }
    bool check_comp(vector<int>& taken_cols, int num){
        for(int i=0;i<taken_cols.size();i++){
            if(taken_cols[i]== num || abs(i-static_cast<int>(taken_cols.size()))== abs(taken_cols[i]-num)){
                return false;
            }
        }
        return true;

    }
};