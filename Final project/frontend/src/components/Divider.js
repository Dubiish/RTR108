import React from "react"
import Navigation from "./Navigation"
import { Container, Jumbotron, Row, Col, Image, Form, Button } from "react-bootstrap"

class Divider extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            resistorZ1 : 0,
            resistorZ2 : 0,
            voltageIn : 0,
            voltageOut : 0
        }

        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        this.setState({
            resistorZ1 : event.target.formResistor1.value,
            resistorZ2 : event.target.formResistor2.value,
            voltageIn : event.target.formVoltage.value,
            voltageOut : this.state.voltageOut
        }, () => {
    
            let data = {
                z1 : this.state.resistorZ1,
                z2 : this.state.resistorZ2,
                voltageIn : this.state.voltageIn
            }
    
            fetch("http://127.0.0.1:5000/divider", {
                method: "POST",
                mode: "cors",
                credentials: "same-origin",
                cache: "no-cache",
                headers: {
                    "Content-Type" : "application/json"
                },
                redirect: "follow",
                referrerPolicy: "no-referrer",
                body: JSON.stringify(data)
            }).then((res) => {
                return res.json();
            }).then((resultData) => {
                this.setState({
                    ...this.state,
                    voltageOut: resultData.result
                });
            })
        });
    }

    render() {
        return(
            <div>
                <Navigation />
                <Jumbotron>
                    <h1 className="display-4 text-center">Voltage divider</h1>
                </Jumbotron>
                <Container>
                    <Row>
                        <Col>
                            <Image src={require("./media/divider.png")} rounded style={{height:"25rem"}} />
                        </Col>
                        <Col>
                            <Row>
                                <Col>
                                    <Form onSubmit={this.handleSubmit}>
                                        <Form.Group>
                                            <h1> Simulation variables </h1>
                                        </Form.Group>
                                        <Form.Group as={Row} controlId="formResistor1">
                                            <Form.Label column sm={4}>Resistor Z(1) [ohm]</Form.Label>
                                            <Col sm={8}>
                                                <Form.Control type="number" placeholder="Enter a value..." />
                                            </Col>
                                        </Form.Group>
                                        <Form.Group as={Row} controlId="formResistor2">
                                            <Form.Label column sm={4}>Resistor Z(2) [ohm]</Form.Label>
                                            <Col sm={8}>
                                                <Form.Control type="number" placeholder="Enter a value..." />
                                            </Col>
                                        </Form.Group>
                                        <Form.Group as={Row} controlId="formVoltage">
                                            <Form.Label column sm={4}>Voltage V(in) [V]</Form.Label>
                                            <Col sm={8}>
                                                <Form.Control type="number" placeholder="Enter a value..." />
                                            </Col>
                                        </Form.Group>
                                        <Button className="float-right" variant="primary" type="submit">Simulate</Button>
                                    </Form>
                                </Col>
                            </Row>
                            <Row>
                                <Col>
                                    <h1>Results</h1>
                                </Col>
                            </Row>
                            <Row>
                                <Col>
                                    <Form.Group as={Row} controlId="resultsResistor1">
                                        <Form.Label column sm={4}>Resistor Z(1) [ohm]</Form.Label>
                                        <Col sm={8}>
                                            <Form.Control readOnly placeholder={this.state.resistorZ1 + " Ohm"} />
                                        </Col>
                                    </Form.Group>
                                    <Form.Group as={Row} controlId="resultsResistor2">
                                        <Form.Label column sm={4}>Resistor Z(2) [ohm]</Form.Label>
                                        <Col sm={8}>
                                            <Form.Control readOnly placeholder={this.state.resistorZ2 + " Ohm"} />
                                        </Col>
                                    </Form.Group>
                                    <Form.Group as={Row} controlId="resultsVoltageIn">
                                        <Form.Label column sm={4}>Voltage V(in) [V]</Form.Label>
                                        <Col sm={8}>
                                            <Form.Control readOnly placeholder={this.state.voltageIn + " V"} />
                                        </Col>
                                    </Form.Group>
                                    <Form.Group as={Row} controlId="resultsVoltageOut">
                                        <Form.Label column sm={4}>Voltage V(out) [V]</Form.Label>
                                        <Col sm={8}>
                                            <Form.Control readOnly placeholder={this.state.voltageOut + " V"} />
                                        </Col>
                                    </Form.Group>
                                </Col>
                            </Row>
                        </Col>
                    </Row>
                </Container>
            </div>
        );
    }
}

export default Divider