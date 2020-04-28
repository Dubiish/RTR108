import React from "react"
import Navigation from "./Navigation"
import { Container, Row, Col, Jumbotron, Card, Button, Spinner } from "react-bootstrap"

class Home extends React.Component {

    render() {
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
                                <Card.Body>
                                    <Card.Title>Voltage Divider</Card.Title>
                                    <Card.Text>Simple voltage divider</Card.Text>
                                    <Button variant="danger" href="/divider"><Spinner as="span" size="sm" animation="grow" role="status" />Simulate</Button>
                                </Card.Body>
                            </Card>
                        </Col>
                        <Col>
                            <Row>
                                <Col>
                                    <Card>
                                        <Card.Body>
                                            <Card.Title>Circuit X</Card.Title>
                                            <Card.Text>Circuit Description</Card.Text>
                                            <Button variant="secondary" href="/divider">Simulate</Button>
                                        </Card.Body>
                                    </Card>
                                </Col>
                            </Row>
                            <Row className="mt-3">
                                <Col>
                                    <Card>
                                        <Card.Body>
                                            <Card.Title>Circuit Y</Card.Title>
                                            <Card.Text>Circuit Description</Card.Text>
                                            <Button variant="secondary" href="/divider">Simulate</Button>
                                        </Card.Body>
                                    </Card>
                                </Col>  
                            </Row>
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    }
}

export default Home