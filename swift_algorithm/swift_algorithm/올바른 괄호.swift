import Foundation

func solution(_ s:String) -> Bool
{
    var ans:Bool = true
    
    var stack: [Character] = []
    
    for char in s {
        if char == ")" {
            guard let last = stack.last, last == "(" else {
                ans = !ans
                break
            }
            stack.removeLast()
            
        } else {
            stack.append(char)
        }
    }

    return 0 < stack.count ? false : ans
}
