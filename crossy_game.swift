import SpriteKit
import GameplayKit

class GameScene: SKScene {
    let laneHeight: CGFloat = 60
    let playerSize: CGFloat = 40
    let carSize = CGSize(width: 60, height: 40)

    var player: SKSpriteNode!
    var cars: [SKSpriteNode] = []
    var spawnTimer: TimeInterval = 0
    var score = 0

    override func didMove(to view: SKView) {
        backgroundColor = SKColor(red: 135/255, green: 206/255, blue: 250/255, alpha: 1)
        physicsBody = SKPhysicsBody(edgeLoopFrom: frame)
        setupPlayer()
    }

    func setupPlayer() {
        player = SKSpriteNode(color: .green, size: CGSize(width: playerSize, height: playerSize))
        player.position = CGPoint(x: frame.midX, y: laneHeight/2)
        addChild(player)
    }

    override func update(_ currentTime: TimeInterval) {
        spawnTimer += 1/60
        if spawnTimer > 0.5 { // roughly every 0.5s
            spawnCar()
            spawnTimer = 0
        }

        for car in cars {
            if car.position.x < -carSize.width || car.position.x > size.width + carSize.width {
                car.removeFromParent()
                if let index = cars.firstIndex(of: car) {
                    cars.remove(at: index)
                }
            }
            if car.frame.intersects(player.frame) {
                gameOver()
            }
        }

        if player.position.y > size.height {
            score += 1
            resetLevel()
        }
    }

    func spawnCar() {
        let laneCount = Int(size.height / laneHeight) - 1
        let lane = Int.random(in: 0..<laneCount)
        let direction: CGFloat = Bool.random() ? 1 : -1

        let car = SKSpriteNode(color: .red, size: carSize)
        let yPos = CGFloat(lane) * laneHeight + laneHeight/2
        let xPos = direction == 1 ? -carSize.width/2 : size.width + carSize.width/2
        car.position = CGPoint(x: xPos, y: yPos)
        addChild(car)
        cars.append(car)

        let speed = CGFloat(Int.random(in: 3...6))
        let moveDistance = size.width + carSize.width
        let duration = TimeInterval(moveDistance / (speed * 60))
        let moveAction = SKAction.moveBy(x: direction * moveDistance, y: 0, duration: duration)
        car.run(SKAction.repeatForever(moveAction))
    }

    func resetLevel() {
        player.position = CGPoint(x: frame.midX, y: laneHeight/2)
        for car in cars {
            car.removeFromParent()
        }
        cars.removeAll()
    }

    func gameOver() {
        player.removeFromParent()
        for car in cars { car.removeAllActions() }
        // Present game over scene or reset
    }

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        guard let touch = touches.first else { return }
        let location = touch.location(in: self)
        let dx = location.x - player.position.x
        let dy = location.y - player.position.y
        if abs(dx) > abs(dy) {
            player.position.x += dx > 0 ? 5 : -5
        } else {
            player.position.y += dy > 0 ? 5 : -5
        }
    }
}
