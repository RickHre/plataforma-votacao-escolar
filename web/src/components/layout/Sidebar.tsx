import { A } from "@solidjs/router";

export default function Sidebar() {
    return (
        <aside class="sidebar">
            <div class="sidebar-logo">
                <span class="sidebar-logo-icon">🧩</span>
                <div>
                    <strong>Votação</strong>
                    <span>Escolar</span>
                </div>
            </div>
            <nav class="sidebar-nav">
                <A href="/admin" activeClass="active" end>
                    <span>▦</span>
                    Dashboard
                </A>
                <A href="/admin/alunos" activeClass="active">
                    <span>♙</span>
                    Alunos
                </A>
                <A href="/admin/candidatos" activeClass="active">
                    <span>♟</span>
                    Candidatos
                </A>
                <A href="/votacao" activeClass="active">
                    <span>✓</span>
                    Votação
                </A>
                <A href="/resultados" activeClass="active">
                    <span>▤</span>
                    Resultados
                </A>
            </nav>
            <div class="sidebar-footer">
                <A href="#">
                    ⚙ Configurações
                </A>
            </div>
        </aside>
    );
}
