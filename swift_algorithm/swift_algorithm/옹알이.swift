import Foundation

func solution(_ babbling:[String]) -> Int {
    
    
    var present:String = ""
    var previous:String = ""
    let wordDict: [String: Int] = ["aya": 0, "ye": 0, "woo": 0, "ma": 0]
    
    var ans:Int = 0
    
    for babbl in babbling {
        for char in babbl {
            present += String(char)
            if wordDict[present] != nil && present != previous {
                previous = present
                present = ""
            }
        }
        
        if present.isEmpty {
            ans += 1
        }
        
        present = ""
        previous = ""
    }
    
    
    return ans
}
