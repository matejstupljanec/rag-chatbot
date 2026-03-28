import { useEffect, useState } from "react";
import type { Message } from "../interfaces/message";
import type { Conversation } from "../interfaces/conversation";

interface Props {
  currentConversation?: Conversation;
}

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

export default function Chat({ currentConversation }: Props) {
  if (!currentConversation) return <div>Greska</div>;

  const [question, setQuestion] = useState<string>("");
  const [messages, setMessages] = useState<Message[]>([]);

  async function handleQuestionSubmit(
    event: React.SyntheticEvent<HTMLFormElement>,
  ) {
    event.preventDefault();

    let userQuestion = question;

    setQuestion("");

    const response = await fetch(
      `${apiBaseUrl}/api/conversations/${currentConversation?.id}/messages`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({
          question: userQuestion,
        }),
      },
    );

    const message = await response.json();

    setMessages([...messages, message]);
  }

  async function getConversationMessages() {
    const response = await fetch(
      `${apiBaseUrl}/api/conversations/${currentConversation?.id}/messages`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      },
    );

    const messages = await response.json();

    setMessages(messages);
  }

  useEffect(() => {
    getConversationMessages();
  }, [currentConversation]);

  return (
    <div>
      <div className="border p-5 m-2">
        {messages.map((message) => (
          <div className="border p-1 flex flex-col mb-2">
            <span className="m-3 p-1 self-end">{message.question}</span>
            <span className="m-3 p-1 self-start">{message.answer}</span>
          </div>
        ))}
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
          <button type="submit" className="ml-2 p-1 border">
            Posalji
          </button>
        </form>
      </div>
    </div>
  );
}
