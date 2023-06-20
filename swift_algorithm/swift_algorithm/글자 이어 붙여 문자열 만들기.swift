import Foundation

func solution(_ my_string:String, _ index_list:[Int]) -> String {
    var answer: String = ""
    let stringArray: [String] = my_string.map { String($0) }
    index_list.forEach { num in
        answer += stringArray[num]
    }
    return answer
}
