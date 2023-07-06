func solution(_ s:String, _  n:Int) -> String {
    
    var ans:String = ""
    
    for char in s {
        let asciiValue = char.asciiValue!
        
        if asciiValue == 32 {
            ans += " "
            continue
        }
        
        let range:UInt8 = asciiValue <= 90 ? 65 : 97
        
        let number:UInt8 = (asciiValue + UInt8(n)) % range
        let string = String(UnicodeScalar( range + (number % 26)))
        ans += string
        
    }
    
    return ans
}

