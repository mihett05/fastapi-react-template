import { clearToken, getToken, setToken } from './storage';

import { baseApiUrl } from '~/shared/config.ts';

class RefreshSynchronizer {
  private refreshCounter = 0;
  private refreshPromise: Promise<string> | null = null;

  public async refreshWithSync(): Promise<string> {
    ++this.refreshCounter;
    if (this.refreshPromise !== null) {
      const response = await this.refreshPromise;
      --this.refreshCounter;
      return response;
    }
    this.refreshPromise = this.refresh();
    const response = await this.refreshPromise;
    --this.refreshCounter;

    this.clearCachedPromise();
    return response;
  }

  private async refresh() {
    const oldToken = getToken();
    if (oldToken === null) {
      throw new Error('Refresh failed');
    }

    const response = await fetch(`${baseApiUrl}/auth/jwt/refresh`, {
      method: 'POST',
      cache: 'no-cache',
      credentials: 'include',
      headers: {
        Authorization: `Bearer ${oldToken}`,
      },
    });
    if (response.status >= 400) {
      clearToken();
      throw new Error('Refresh failed');
    }
    const body = (await response.json()) as { accessToken: string };
    if (!body.accessToken) {
      clearToken();
      throw new Error('Refresh failed');
    }
    setToken(body.accessToken);
    return body.accessToken;
  }

  private clearCachedPromise() {
    if (this.refreshCounter > 0) {
      setTimeout(this.clearPromise, 500);
    } else {
      this.clearPromise();
    }
  }

  private clearPromise() {
    this.refreshPromise = null;
    this.refreshCounter = 0;
  }
}

const lock = new RefreshSynchronizer();

export const refreshToken = () => lock.refreshWithSync();
