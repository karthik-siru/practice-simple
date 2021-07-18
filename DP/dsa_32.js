
/**
 *  Idea : 
 *      This is a variation of CoinChange problem , 
 *      ->  there , we found minimum number of coins to make change 
 * 
 *      Strategy : 
 *      ->  we can choose any number of coins of same value 
 *          but once we move we cannot choose that coin .
 *        
 *      ->  the first loop handles ,when we can choose only coin of value 3 .
 *      ->  second loop for 5 and so on .
 */


/**
 * @param {number} n
 * @returns {number}
*/

class Solution{
    count(n){
        //code here
        var dp = new Array();
        
        for (let i =0  ; i< n+1 ; i++){
            
           dp.push(0)
        }
        
        dp[0]  =  1 ; 
        
        // when we have only coins of value 3 
        for(let  i =3 ; i<  n+1 ;  i ++)
            dp[i]  += dp[i-3]
        // when we have 3 and 5 value coins 
        for(let  i =5 ; i<  n+1 ;  i ++)
            dp[i]  += dp[i-5]
        // when we have 3 and 5 and 10 coins 
        for(let  i =10 ; i<  n+1 ;  i ++)
            dp[i]  += dp[i-10]
            
        
        
        return dp[dp.length -1 ]
    }
}