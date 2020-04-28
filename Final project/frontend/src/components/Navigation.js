import React from "react"
import { Nav, Navbar, NavDropdown } from "react-bootstrap"

function Navigation() {
    return(
        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="/">Simulator</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <NavDropdown title="Circuits" id="basic-nav-dropdown">
                        <NavDropdown.Item href="/divider">Voltage Divider</NavDropdown.Item>
                        <NavDropdown.Item href="#" disabled>Circuit X</NavDropdown.Item>
                        <NavDropdown.Item href="#" disabled>Circuit Y</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}

export default Navigation