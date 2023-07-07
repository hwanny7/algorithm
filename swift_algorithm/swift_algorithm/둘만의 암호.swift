import Foundation

func solution(_ s:String, _ skip:String, _ number:Int) -> String {
    var skipArray: [Bool] = Array(repeating: true, count: 26)
    var ans: String = s
    skip.forEach { (value) in
        let index:Int = Int(value.asciiValue! % 97)
        skipArray[index] = false
    }
    
    return ans.map {
        let index:Int = Int($0.asciiValue! % 97)
        var plus:Int = 0
        var count:Int = 0
        
        while count < number {
            plus += 1
            if skipArray[(index + plus) % 26] {
                count += 1
            }
        }
        
        return String(UnicodeScalar(97 + (index + plus) % 26)!)
        
    }.joined()
}
