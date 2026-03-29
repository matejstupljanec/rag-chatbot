import { useEffect, useState } from "react";
import type { Conversation } from "../interfaces/conversation";

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

interface Props {
  currentConversation?: Conversation;
  onCurrentConversationChange: (conversation: Conversation) => void;
}

export default function Sidebar({
  currentConversation,
  onCurrentConversationChange,
}: Props) {
  const [conversations, setConversations] = useState<Conversation[]>([]);

  async function getConversations() {
    const response = await fetch(`${apiBaseUrl}/api/conversations`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });

    const conversations = await response.json();

    setConversations(conversations);
  }

  async function createConversation() {
    const response = await fetch(`${apiBaseUrl}/api/conversations`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({}),
    });

    const conversation = await response.json();

    setConversations([conversation, ...conversations]);
    onCurrentConversationChange(conversation);
  }

  useEffect(() => {
    getConversations();
  }, []);

  useEffect(() => {
    if (conversations.length > 0) {
      onCurrentConversationChange(conversations[0]);
    }
  }, [conversations]);

  return (
    <div className="flex flex-col p-2 bg-darkblue text-white overflow-hidden">
      <div className="mt-5 mb-5">
        <button
          className="flex flex-row items-center p-2 w-full hover:bg-lightblue rounded-xl cursor-pointer"
          onClick={createConversation}
        >
          <div className="w-5.5 h-5.5">
            <svg
              width="100%"
              height="100%"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M12 8V16M8 12H16M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </div>
          <div className="text-xl ml-2">Novi razgovor</div>
        </button>
      </div>
      <div className="flex flex-col min-h-0 text-lg">
        <div className="p-2">
          <span className="border-b pb-1 opacity-60">Nedavni razgovori</span>
        </div>
        <ul className="overflow-y-auto scrollbar scrollbar-thumb-gray-600 scrollbar-track-gray-600">
          {conversations.map((conversation) => (
            <li
              key={conversation.id}
              onClick={() => {
                onCurrentConversationChange(conversation);
              }}
              className={`p-2 pt-1 pb-1 mb-1 w-full rounded-xl select-none cursor-pointer ${currentConversation && conversation.id === currentConversation.id ? "bg-lightblue" : "hover:bg-lightblue"}`}
            >
              {conversation.name}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
