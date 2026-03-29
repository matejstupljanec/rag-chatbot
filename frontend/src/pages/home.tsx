import { useState } from "react";

import Chat from "../components/chat";
import Header from "../components/header";
import Sidebar from "../components/sidebar";
import SidebarHeader from "../components/sidebar_header";
import type { Conversation } from "../interfaces/conversation";

export default function Home() {
  const [currentConversation, setCurrentConversation] =
    useState<Conversation>();
  return (
    <div className="grid grid-cols-[270px_1fr] grid-rows-[50px_1fr] h-screen overflow-hidden">
      <SidebarHeader />
      <Header />
      <Sidebar
        currentConversation={currentConversation}
        onCurrentConversationChange={setCurrentConversation}
      />
      <Chat currentConversation={currentConversation} />
    </div>
  );
}
