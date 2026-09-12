import { createSignal } from "solid-js";
import { useNavigate } from "@solidjs/router";

import AuthLayout from "../layouts/AuthLayout";
import Input from "../components/ui/Input";
import Button from "../components/ui/Button";

export default function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = createSignal("");
    const [password, setPassword] = createSignal("");

    function handleSubmit(
        event: SubmitEvent
    ) {
        event.preventDefault();

        console.log({
            username: username(),
            password: password()
        });

        // Temporário.
        // Posteriormente será substituído
        // pela autenticação real.

        navigate("/votacao");
    }

    return (
        <AuthLayout>
            <div class="login-card">
                <div class="login-header">
                    <div class="login-logo">🧩</div>
                    <h1>
                        Votação Escolar
                    </h1>
                    <p>
                        Plataforma de votação
                    </p>
                </div>
                <form class="login-form" onSubmit={handleSubmit}>
                    <Input
                        label="Usuário"
                        placeholder="Digite seu usuário"
                        value={username()}
                        onInput={(event) =>
                            setUsername(
                                event.currentTarget.value
                            )
                        }
                    />
                    <Input
                        label="Senha"
                        type="password"
                        placeholder="Digite sua senha"
                        value={password()}
                        onInput={(event) =>
                            setPassword(
                                event.currentTarget.value
                            )
                        }
                    />
                    <Button type="submit">
                        Entrar
                    </Button>
                </form>
                <div class="login-links">
                    <a href="#">
                        Esqueci minha senha
                    </a>
                    <a href="/admin">
                        Acesso do professor
                    </a>
                </div>
            </div>
        </AuthLayout>
    );
}
