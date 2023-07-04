import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var nameDict: [String:Int] = [:]
    var players: [String] = players
    
    for (index, name) in players.enumerated() {
        nameDict[name] = index
    }
    
    for name in callings {
        let index:Int = nameDict[name]!
        let aheadName:String = players[index - 1]
        
        nameDict[name]! -= 1
        nameDict[aheadName]! += 1
        
        players[index] = aheadName
        players[index - 1] = name
        
        
    }
    
    
    return players
}
