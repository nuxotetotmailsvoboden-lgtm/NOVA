import { api } from "@/lib/api/client";
import type {
  Client,
  ApiResponse,
  PaginatedResponse,
} from "@/lib/api/types";

export interface GetClientsParams {
  page?: number;
  pageSize?: number;
  search?: string;
  status?: string;
}

export const clientsApi = {
  getAll(params?: GetClientsParams) {
    return api.get<ApiResponse<PaginatedResponse<Client>>>(
      "/crm/clients",
      params
    );
  },

  getById(id: string) {
    return api.get<ApiResponse<Client>>(
      `/crm/clients/${id}`
    );
  },

  create(data: Partial<Client>) {
    return api.post<ApiResponse<Client>>(
      "/crm/clients",
      data
    );
  },

  update(id: string, data: Partial<Client>) {
    return api.put<ApiResponse<Client>>(
      `/crm/clients/${id}`,
      data
    );
  },

  delete(id: string) {
    return api.delete<ApiResponse<void>>(
      `/crm/clients/${id}`
    );
  },
};
