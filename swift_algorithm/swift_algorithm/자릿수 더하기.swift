import Foundation

func solution(_ n:Int) -> Int
{
    var num: Int = n
    var ans: Int = 0
    
    while num > 0 {
        ans += num % 10
        num /= 10
    }
    return ans
}
