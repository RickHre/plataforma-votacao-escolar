import { A } from "@solidjs/router";

export default function NotFound() {
    return (
        <main class="not-found">
            <h1>
                404
            </h1>
            <p>
                Página não encontrada.
            </p>
            <A href="/">
                Voltar para o início
            </A>
        </main>
    );
}
