export interface Message {
  id: number;
  question: string;
  answer: string;
  liked_at: string;
  disliked_at: string;
  answered_at: string;
  failed_at: string;
  sources: JSON;
  conversation_id: number;
  created_at: string;
  updated_at: string;
}
