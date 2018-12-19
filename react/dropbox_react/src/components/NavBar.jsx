import React from 'react';
import {
    Collapse,
    Navbar,
    NavbarBrand,
    Nav,
    NavItem,
    Button
} from 'reactstrap';
import {withRouter, Link} from "react-router-dom";

class NavBar extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            isAuthorized: localStorage.getItem('token'),
            disabled_login:false,
            disabled_register:false
        }
    }

    handleRegistration = () => {
        let path = '/register';
        this.props.history.push(path);
    };

    handleSignIn = () => {
        let path = '/login';
        this.props.history.push(path);
    };
    
    handleLogout = () =>{
        let path = '/login';
        this.props.history.push(path);
        this.setState({
            token:localStorage.removeItem('token'),
            id:localStorage.removeItem('id')});
    };

    render() {
        if (this.state.isAuthorized)
            return (
                <div className>
                    <Navbar color="dark"  expand="sm" fixed='top'>
                        <NavbarBrand>
                            <Link to='/'>Flask Dropbox</Link>
                        </NavbarBrand>
                        <Collapse navbar>
                            <Nav className="ml-auto" navbar>
                                <NavItem>
                                    <Button className='mdc-button-sm mdc-button--raised m-1' onClick={this.handleLogout}>Logout</Button>
                                </NavItem>
                            </Nav>
                        </Collapse>
                    </Navbar>
                </div>
            );
        else {
            return(
                <div className>
                    <Navbar color="dark"  expand="sm">
                        <NavbarBrand>
                            <Link to='/'>Flask Dropbox </Link>
                        </NavbarBrand>
                        <Collapse navbar>
                            <Nav className="ml-auto" navbar>
                                <NavItem>
                                    <Button disabled={this.state.disabled_register} className='mdc-button-sm mdc-button--raised m-1'
                                            onClick={this.handleRegistration}> Register
                                    </Button>
                                </NavItem>
                                <NavItem>
                                    <Button disabled={this.state.disabled_login} className='mdc-button-sm mdc-button--raised m-1'
                                            onClick={this.handleSignIn}> Login
                                    </Button>
                                </NavItem>
                            </Nav>
                        </Collapse>
                    </Navbar>
                </div>
            )
        }
    }
}

export default withRouter(NavBar)