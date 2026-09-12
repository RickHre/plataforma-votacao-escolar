import { Route, Router } from "@solidjs/router";

import Login from "./pages/Login";
import Voting from "./pages/Voting";
import Results from "./pages/Results";
import Dashboard from "./pages/Dashboard";
import Students from "./pages/Students";
import Candidates from "./pages/Candidates";
import NotFound from "./pages/NotFound";

import DashboardLayout from "./layouts/DashboardLayout";

export default function App() {
    return (
        <Router>
            {/* Área pública */}
            <Route path="/" component={Login}/>
            <Route path="/votacao" component={Voting}/>
            <Route path="/resultados" component={Results}/>

            {/* Área administrativa */}
            <Route path="/admin" component={DashboardLayout}>
                <Route path="/" component={Dashboard}/>
                <Route path="/alunos" component={Students}/>
                <Route path="/candidatos" component={Candidates}/>
            </Route>

            <Route path="*" component={NotFound}/>
        </Router>
    );
}
