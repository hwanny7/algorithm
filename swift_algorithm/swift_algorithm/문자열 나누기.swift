import Foundation

func solution(_ s:String) -> Int {
    
    var x:Character = s[s.index(s.startIndex, offsetBy: 0)]
    
    var xCount:Int = 0
    var yCount:Int = 0
    var ans:Int = 0

    
    for index in 0..<s.count {
        let char: Character = s[s.index(s.startIndex, offsetBy: index)]
        if xCount == 0 {
            xCount = 1
            x = char
            continue
        }
        
        
        if char == x {
            xCount += 1
        } else {
            yCount += 1
        }
        
        if xCount == yCount {
            ans += 1
            xCount = 0
            yCount = 0
        }
        
        
    }
    
    return xCount > 0 ? ans + 1 : ans
}
