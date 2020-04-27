import React from "react"
import { Nav, Navbar } from "react-bootstrap"

function Navigation() {
    return(
        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="/">Simulator</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href="/divider">Voltage Divider</Nav.Link>
                    <Nav.Link href="#" disabled>Circuit 2</Nav.Link>
                    <Nav.Link href="#" disabled>Circuit 3</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default Navigation