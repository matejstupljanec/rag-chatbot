import { useState } from "react";


const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

interface Message {
    question: string,
    answer: string
}

export default function Chat() {
    const [question, setQuestion] = useState<string>("")
    const [messages, setMessages] = useState<Message[]>([])

    async function handleQuestionSubmit(event: React.SyntheticEvent<HTMLFormElement>) {
        event.preventDefault();

        console.log(question)

        const response = await fetch(`${apiBaseUrl}/api/questions`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify({
                question: question
            })

        })

        const data = await response.json()

        console.log(data.answer)

        const newMessage: Message = {
            question: question,
            answer: data.answer
        }

        setMessages([...messages, newMessage])

        console.log(messages)


        setQuestion('')
    }

    return (
        <div>
            <div className="border p-5 m-2">
                {messages.map(message =>
                    <div className="border p-1 flex flex-col mb-2">
                        <span className="m-3 p-1 self-end">{message.question}</span>
                        <span className="m-3 p-1 self-start">{message.answer}</span>
                    </div>
                )}

            </div>

            <div className="border p-5 m-2 flex justify-center">
                <form onSubmit={handleQuestionSubmit}>
                    <input
                        type="text"
                        name="question"
                        value={question}
                        placeholder="Postavi pitanje..."
                        onChange={(e) => setQuestion(e.target.value)}
                        required
                        className="p-1 border w-100"
                    />
                    <button type="submit" className="ml-2 p-1 border">Posalji</button>
                </form>
            </div>
        </div >
    )

}