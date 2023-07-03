import Foundation

func solution(_ number:[Int]) -> Int {
    let length: Int = number.count
    var ans: Int = 0
    for i in 0...length - 3 {
        for j in (i+1)..<length {
            for k in (j+1)..<length {
                if number[i] + number[j] + number[k] == 0 { ans += 1}
            }
        }
    }
    
    
    
    
    
    return ans
}
