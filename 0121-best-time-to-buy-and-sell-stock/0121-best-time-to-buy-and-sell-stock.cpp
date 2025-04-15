class Solution {
public:
    int maxProfit(vector<int>& prices) {
      int lp=INT_MAX;
      int op=0;
      int prof=0;
      for(int i=0;i<prices.size();i++)
      {
        if(prices[i]<lp){
            lp=prices[i];
        }
        prof=prices[i]-lp;
        if(op<prof){
            op=prof;
        }
      } 
      return op; 
    }
};