import { For } from "solid-js";

import PageHeader from "../components/layout/PageHeader";

import Button from "../components/ui/Button";

import Card from "../components/ui/Card";

import Badge from "../components/ui/Badge";

const students = [
    {
        id: 1,
        name: "João da Silva",
        username: "joao",
        active: true
    },
    {
        id: 2,
        name: "Maria Oliveira",
        username: "maria",
        active: true
    },
    {
        id: 3,
        name: "Carlos Souza",
        username: "carlos",
        active: false
    }
];

export default function Students() {
    return (
        <div>
            <PageHeader
                title="Alunos"
                description="Gerencie os alunos cadastrados"
                action={
                    <Button>Novo aluno</Button>
                }
            />
            <Card>
                <div class="table-wrapper">
                    <table>
                        <thead>
                            <tr>
                                <th>Nome</th>
                                <th>Usuário</th>
                                <th>Status</th>
                                <th>Ações</th>
                            </tr>
                        </thead>
                        <tbody>
                            <For each={students}>
                                {(student) => (
                                    <tr>
                                        <td>
                                            {student.name}
                                        </td>
                                        <td>
                                            {student.username}
                                        </td>
                                        <td>
                                            {student.active ? (
                                                <Badge variant="success">Ativo</Badge>
                                            ) : (
                                                <Badge variant="danger">Inativo</Badge>
                                            )}
                                        </td>
                                        <td>
                                            <Button variant="secondary">
                                                Editar
                                            </Button>
                                        </td>
                                    </tr>
                                )}
                            </For>
                        </tbody>
                    </table>
                </div>
            </Card>
        </div>
    );
}
