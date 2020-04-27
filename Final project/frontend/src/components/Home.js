import React from "react"
import Navigation from "./Navigation"
import { Container, Row, Col, Jumbotron, Card, Button } from "react-bootstrap"

function Home() {
    return(
        <div>
            <Navigation />
            <Jumbotron className="text-center">
                <h1 className="display-4">Circuit Simulator</h1>
                <p>This is a web application made for Computer Studies course</p>
            </Jumbotron>
            <Container>
                <Row>
                    <Col>
                        <Card>
                            <Card.Img variant="top" src={require("./media/divider.png")} style={{height:"25rem"}} />
                            <Card.Body>
                                <Card.Title>Voltage Divider</Card.Title>
                                <Card.Text>Simple voltage divider</Card.Text>
                                <Button variant="primary" href="/divider">Simulate</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card>
                            <Card.Img variant="top" src={require("./media/divider.png")} style={{height:"25rem"}} />
                            <Card.Body>
                                <Card.Title>Circuit Name</Card.Title>
                                <Card.Text>Circuit Description</Card.Text>
                                <Button variant="primary" href="/divider" disabled>Simulate</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col>
                        <Card>
                            <Card.Img variant="top" src={require("./media/divider.png")} style={{height:"25rem"}} />
                            <Card.Body>
                                <Card.Title>Circuit Name</Card.Title>
                                <Card.Text>Circuit Description</Card.Text>
                                <Button variant="primary" href="/divider" disabled>Simulate</Button>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        </div>
    );
}

export default Home